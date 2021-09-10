import openpyxl as op

class XlCompare_SingleWorbook:
    def __init__(self, path):
        self.wb = op.load_workbook(path)

    # returns 2D list of values unique to each column 
    def compareCols_unique(self, sheetName, col1, col2):
        sheet = self.wb[sheetName]
        col1_values = []
        col2_values = []
        result = [[],[]]

        for cell in sheet[col1]:
            col1_values.append(cell.value)

        for cell in sheet[col2]:
            col2_values.append(cell.value)

        for x in col1_values:
            if x not in col2_values:
                result[0].append(x)
        
        for x in col2_values:
            if x not in col1_values:
                result[1].append(x)

        return result



        


    