import rki
import fastapi

df = rki.load_data()

# log IP adresses ? fastapi

app = 


@app.get
def get_cases_last7days(day, state="Gesamt"):
    day_datetime = parse(day)
    return df.loc[day_datetime, state]

def get_all_last7days(state="Gesamt"):
    return df[state]