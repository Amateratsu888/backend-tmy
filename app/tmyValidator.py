class SchemaValidator(object):
    def __init__(self, response={}):
        self.response  =response
 
    def isTrue(self):
 
        errorMessages = []
 
        try:
            # Validation for project_name field
            project_name = self.response.get("project_name", None)
            if project_name is None or len(project_name) <= 1:
                raise Exception("Error")
        except Exception as e:
            errorMessages.append("Field project_name is required ")

        try:
            # Validation for location field
            location = self.response.get("location", {})
            latitude = location.get("latitude")
            longitude = location.get("longitude")
            altitude = location.get("altitude")

            if (
                not (isinstance(latitude, float) and -90 <= latitude <= 90) or
                not (isinstance(longitude, float) and -180 <= longitude <= 180) or
                not (isinstance(altitude, int) and altitude >= 0)
            ):
                raise Exception("Error")
        except Exception as e:
            errorMessages.append("Invalid location data")

        try:
            # Validation for pv_system field
            pv_system = self.response.get("pv_system", {})
            technology = pv_system.get("technology")

            if technology not in ["pv", "tracker"]:
                raise Exception("Error")

            if technology == "pv":
                pv_data = pv_system.get("pv", {})
                tilt = pv_data.get("tilt")
                azimuth = pv_data.get("azimuth")

                if (
                    not (isinstance(tilt, int) and 0 <= tilt <= 90) or
                    not (isinstance(azimuth, int) and 0 <= azimuth <= 360)
                ):
                    raise Exception("Error")
            elif technology == "tracker":
                tracker_data = pv_system.get("tracker", {})
                gcr = tracker_data.get("gcr")
                axis_azimuth = tracker_data.get("axis_azimuth")
                max_angle = tracker_data.get("max_angle")

                if (
                    not (isinstance(gcr, float) and 0 <= gcr <= 1) or
                    not (isinstance(axis_azimuth, int) and 0 <= axis_azimuth <= 360) or
                    not (isinstance(max_angle, int) and 0 <= max_angle <= 360)
                ):
                    raise Exception("Error")
        except Exception as e:
            errorMessages.append("Invalid pv_system data")

        try:
            # Validation for analysis field
            analysis = self.response.get("analysis", {})

            probabilities = analysis.get("probabilities", {})
            valid_probabilities = ["P50", "P75", "P90", "P10", "P99"]

            for key, value in probabilities.items():
                if key not in valid_probabilities or not isinstance(value, bool):
                    raise Exception("Error")

            meteo_data = analysis.get("meteo_data", {})
            valid_meteo_data = [
                "ambient_temperature",
                "pm_2_5",
                "pm_10",
                "relative_humidity",
                "precipitable_water",
                "wind_direction",
            ]

            for key, value in meteo_data.items():
                if key not in valid_meteo_data or not isinstance(value, bool):
                    raise Exception("Error")

            granularity = analysis.get("granularity")
            valid_granularities = ["5 minutes", "15 minutes", "hourly"]

            if granularity not in valid_granularities:
                raise Exception("Error")
        except Exception as e:
            errorMessages.append("Invalid analysis data")

 
 
        return errorMessages
 