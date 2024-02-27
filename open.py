import webbrowser
import sys

software_engineer = ["https://leetcode.com/problemset/", "https://www.linkedin.com/feed/", "https://chat.openai.com","https://www.freecodecamp.org/learn"]
job1 = ["https://auth.edgenuity.com/Login/Login/Educator","https://magenta.oasesonline.com/?_gl=1*14wrc9v*_gcl_au*NTM1NzkxNTU3LjE2OTcwMDMxMjY.*_ga*MTk0NDgyNjcxNy4xNjk3MDAzMTI2*_ga_ZWQVC3NWZC*MTY5ODIxODQ2NS43LjEuMTY5ODIxOTAyNi41OS4wLjA.&_ga=2.173673252.604550291.1698160072-1944826717.1697003126"]
job2 = ["https://drive.google.com/drive/u/2/folders/11fZM855xGNSW0Qnaj4CGKs-Sm9I3rDqb","https://magikidlab.com/teacher-center"]
invest = ["https://www.tradingview.com/chart/k6yafcnF/?symbol=SP%3ASPX"]


def open_tabs(urls):
    first = 0
    for url in urls:
        if first == 0:
            webbrowser.open_new(url)
        else:    
            webbrowser.open_new_tab(url)
        first += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python open.py <#>")
    
    select = sys.argv[1]

    if select == "1":
        open_tabs(software_engineer)
    elif select == "2":
        open_tabs(job1)
    elif select == "3":
        open_tabs(job2)
    elif select == "4":
        open_tabs(invest)