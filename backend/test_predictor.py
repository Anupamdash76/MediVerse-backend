from services.predictor import predictor

result = predictor.predict(

    [
        "fever",
        "headache",
        "vomiting"
    ]

)

print(result)