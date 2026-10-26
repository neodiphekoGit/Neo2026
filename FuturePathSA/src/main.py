import flet as ft
from pages.accounting import get_accounting_view  
from pages.Business import get_business_view
from pages.civil import get_civil_engineering_view
from pages.cybersecurityandIT import get_cybersecurity_View
from pages.datascience import get_datascience_View
from pages.electrical import get_electrical_eng_view
from pages.electricaltrade import get_electrical_trade_view
from pages.hospitality import get_hospitality
from pages.humanresource import get_hr_view
from pages.logistics import get_logistics_view
from pages.mechanical import get_mechanical_eng_view
from pages.medicallab import get_medical_lab_view
from pages.motormechanics import get_motormechanics_view
from pages.nursing import get_nursing_view
from pages.pharmacy import get_pharmacy_view
from pages.plumbing import get_plumbing_view
from pages.renewable import get_renewable_view
from pages.softwaredevelopment import get_software_development_view
from pages.welding import get_welding_view
from pages.agriculture import get_agriculture_view


def main(page: ft.Page):
    page.title = "Course Dashboard"
    page.padding = 20
    page.bgcolor = "#F5F6F9"

    # Add an app bar
    page.appbar = ft.AppBar(
        title=ft.Column(
            [
                ft.Text("Future Path SA", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Top 20 Courses for Better Job opportunities", size=14, italic=True),
                ft.Text("Choose the right course. Build your future", size=14, italic=True),
            ],  
            spacing=2, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,      
        ),
        bgcolor="#000080",
        color=ft.Colors.WHITE,
        center_title=True,
        toolbar_height=70,
    )

    course_titles = [
        "Software Development",
        "Cybersecurity and Information Technology",
        "Data Science and Data Analytics",
        "Electrical Engineering",
        "Civil Engineering and Construction",
        "Mechanical Engineering",
        "Renewable Energy Technology",
        "Nursing",
        "Medical Laboratory Science",
        "Pharmacy",
        "Accounting and Financial Management",
        "Logistics and Supply Chain Management",
        "Human Resource Management",
        "Business Management",
        "Hospitality Management and Professional Cookery",
        "Agriculture and Agricultural Management",
        "Plumbing",
        "Electrical Trade / Electrician",
        "Welding and Boilermaking",
        "Motor Mechanics / Automotive Repair"
    ]

    # Create the main grid view (Home Page)
    grid = ft.GridView(
        expand=True,
        runs_count=4,            
        max_extent=350,           
        child_aspect_ratio=3.0,  
        spacing=12,              
        run_spacing=12,          
        controls=[]
    )

    for title in course_titles:
        card = ft.Card(
            elevation=2,
            bgcolor="white",
            content=ft.ListTile(
                leading=ft.Icon(ft.Icons.SCHOOL, color="blue900", size=24), 
                title=ft.Text(title, weight="bold", size=13, color="blue900"),
                on_click=lambda e, t=title: navigate_based_on_title(e, t)
            )
        )
        grid.controls.append(card)

    # Function to switch views directly by changing page controls
    def navigate_based_on_title(e, title):
        clean_title = title.lower()
        page.clean()  # Clear current items on the screen

        # If Accounting is clicked, display your custom accounting view
        if "accounting" in clean_title:
            page.add(get_accounting_view(lambda _: go_home())) 

        elif "business" in clean_title:
            page.add(get_business_view(lambda _: go_home())) 
        elif "civil" in clean_title or "construction"   in clean_title: 
            page.add(get_civil_engineering_view(lambda _: go_home())) 

        elif "cybersecurity" in clean_title or "IT"   in clean_title: 
            page.add(get_cybersecurity_View(lambda _: go_home())) 

        elif "data science" in clean_title or "data analytics" in clean_title: 
            page.add(get_datascience_View(lambda _: go_home())) 

        elif "electrical" in clean_title: 
            page.add(get_electrical_eng_view(lambda _: go_home())) 

        elif "electrical trade" in clean_title or "electrician" in clean_title: 
            page.add(get_electrical_trade_view(lambda _: go_home())) 

        elif "hospitality" in clean_title: 
            page.add(get_hospitality(lambda _: go_home())) 

        elif "human resource management" in clean_title: 
            page.add(get_hr_view(lambda _: go_home())) 

        elif "logistics" in clean_title or "supply chain" in clean_title: 
            page.add(get_logistics_view(lambda _: go_home())) 

        elif "mechanical engineering" in clean_title: 
            page.add(get_mechanical_eng_view(lambda _: go_home())) 

        elif "medical laboratory science" in clean_title: 
            page.add(get_medical_lab_view(lambda _: go_home())) 

        elif "motor mechanics" in clean_title or "automotive repairs" in clean_title: 
            page.add(get_motormechanics_view(lambda _: go_home()))

        elif "medical laboratory science" in clean_title: 
            page.add(get_medical_lab_view(lambda _: go_home())) 

        elif "nursing" in clean_title:
            page.add(get_nursing_view(lambda _: go_home())) 

        elif "pharmacy" in clean_title:
            page.add(get_pharmacy_view(lambda _: go_home())) 

        elif "plumbing" in clean_title:
            page.add(get_plumbing_view(lambda _: go_home())) 

        elif "renewable energy" in clean_title:
            page.add(get_renewable_view(lambda _: go_home())) 

        elif "software development" in clean_title:
            page.add(get_software_development_view(lambda _: go_home())) 

        elif "welding" in clean_title or "boiler making" in clean_title:
            page.add(get_welding_view(lambda _: go_home())) 
        
        elif "agriculture" in clean_title or "agricultural" in clean_title:
            page.add(get_agriculture_view(lambda _: go_home())) 

    
    
    




    
    
    

            
        """else:
            # Fallback screen for other courses until their views are built
            page.add(
                ft.Column([
                    ft.ElevatedButton("← Back to Dashboard", on_click=lambda _: go_home()),
                    ft.Divider(),
                    ft.Text(f"Welcome to {title}", size=24, weight="bold"),
                    ft.Text("Course content coming soon...", size=16, italic=True)
                ], expand=True)
            )"""
        page.update()

    # Function to return back to the main course grid
    def go_home():
        page.clean()
        page.add(grid)
        page.update()

    # Initial load
    page.add(grid)
    page.update()

if __name__ == "__main__":
    ft.run(main)