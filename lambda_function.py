import pandas as pd
lambda_handler(event, context):

    d = {"col1":[1,2],"col2":[3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print("done x.1")