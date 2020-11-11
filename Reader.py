class Reader:
    """
        Class for reading a file
    """
    def __init__(self, file_name: str):
        self.file_name = file_name

    def get_from_file(self) -> iter:
        """
        return iterator lines of file
        """
        with open(self.file_name, 'r') as file:
            return (tuple(line.split()) for line in file.readlines() if line != '\n')

