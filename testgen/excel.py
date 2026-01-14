
from openpyxl import Workbook
def generate(screen,path):
    wb=Workbook();ws=wb.active
    ws.append(['Category','Sub Category','Feature','Title','Description',
               'Precondition','Steps','Expected Result','Actual Result','Comments'])
    for s in screen.states:
        for c in s.components:
            ws.append(['Camera','Settings',screen.name,f'Verify {c.label}',
                       f'{c.label} in {s.name}','App launched',
                       f'Open {screen.name}',f'{c.label} visible','',''])
    wb.save(path)
