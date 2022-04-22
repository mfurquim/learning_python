class MissingSonicVersion(Exception):
    """ Exception raised for missing sonic version information on DataFrame

    Attr:
        df (pd.DataFrame): DataFrame to store
        message (str): Explanation of the error - e.g., 'Missing sonic version information on DataFrame'
    """

    def __init__(self, df, message="Missing sonic version information on DataFrame"):
        self.df = df
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Columns: {self.df.columns}"
