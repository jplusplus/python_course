# coding: utf-8
def write_weather_report(degrees, cloudiness):
    if degrees < 20:
        print("Det är kylslaget i dag, bara %s grader, och %s"
              % (degrees, cloudiness))
    elif cloudiness == "strålande sol":
        print("Vilket väder! %s grader varmt, och dessutom strålande sol!"
              % cloudiness)
    else:
        print("Det är %s grader och %s" % (degrees, cloudiness))

write_weather_report(20, "molnigt")
write_weather_report(15, "halvklart")
write_weather_report(27, "strålande sol")
write_weather_report(12, "strålande sol")
