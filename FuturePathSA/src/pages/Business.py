import os
from dotenv import load_dotenv
import flet as ft
import requests

# 1. Load environment variables from the .env file
load_dotenv()
API_TOKEN = os.getenv("MY_SECRET_TOKEN")
API_URL = "https://quickmock.dev/m/vrav5kZZiGwz"

# Initialize variables to avoid UnboundLocalError if the request fails
qual_name = "Unknown Qualification"
APS = "N/A"
course_type = "N/A"
qual_type = "N/A"
subject1 = "N/A"
subject1_marks = "N/A"
subject2 = "N/A"
subject2_marks = "N/A"
careers = "N/A"
response = None


def format_qual_name(data_input):
    if isinstance(data_input, list):
        return ", ".join(str(item) for item in data_input).upper()
    elif data_input:
        return str(data_input).upper()
    return "Institution not found"


try:
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json",
    }
    response = requests.get(API_URL, headers=headers)
except Exception as e:
    print(f"Error: {e}")

if response and response.status_code == 200:
    data = response.json()
    raw_qual_name = None

    for inst in data:
        if str(inst["id"]) == "14":
            raw_qual_name = inst["institution"]
            APS = inst["minimum_aps"]
            raw_course_type = inst["qualification_type"]
            subject1 = inst["subject1"]
            subject1_marks = inst["subject1_marks"]
            subject2 = inst["subject2"]
            subject2_marks = inst["subject2_marks"]
            raw_qual_type = inst["qualification_type"]
            raw_careers = inst["possible_careers"]
            break
        else:
            raw_qual_name = "Institution not found"

    qual_name = format_qual_name(raw_qual_name)
    course_type = format_qual_name(raw_course_type)
    qual_type = format_qual_name(raw_qual_type)
    careers = format_qual_name(raw_careers)


def get_business_view(on_back_click):
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        controls=[
            # App bar at the top with a title
            ft.AppBar(
                title=ft.Text("Business Management", size=18),
                bgcolor=ft.Colors.BLUE_900,
                color=ft.Colors.WHITE,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextButton(
                            content="Back to Dashboard",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=on_back_click,
                        ),
                        ft.Divider(height=5),
                        # Institutions offering the course (smaller heading)
                        ft.Text(
                            f"Institutions: 🏫 {qual_name}",
                            size=16,
                            weight="bold",
                        ),
                        # APS Score and Qualification Type cards (compact)
                        ft.Row(
                            controls=[
                                # Minimum APS Score card
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(
                                                "Minimum APS Score",
                                                size=14,
                                                weight="bold",
                                            ),
                                            ft.Text(
                                                f"{APS}",
                                                size=13,
                                                weight="bold",
                                                color=ft.Colors.BLUE_900,
                                            ),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=4,
                                    ),
                                    bgcolor="#EAF2FF",
                                    padding=10,
                                    border_radius=10,
                                    expand=True,
                                ),
                                # Qualification Type card
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(
                                                "Qualification Type",
                                                size=14,
                                                weight="bold",
                                            ),
                                            ft.Text(
                                                f"{course_type}",
                                                size=13,
                                                weight="bold",
                                                color=ft.Colors.GREEN_800,
                                            ),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=4,
                                    ),
                                    bgcolor="#E7F7EF",
                                    padding=10,
                                    border_radius=10,
                                    expand=True,
                                ),
                            ],
                            spacing=8,
                        ),
                    ],
                    spacing=8,
                ),
                padding=10,
            ),
            # Card displaying Mandatory School Subjects (compact)
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "Mandatory School Subjects",
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_900,
                        )
                    ]
                ),
                bgcolor="#E3EEFF",
                padding=10,
                border_radius=8,
                width=float("inf"),
            ),
            # Display required subjects and minimum grade required (compact)
            ft.Container(
                content=ft.Row(
                    controls=[
                        # --- Column 1: Subjects ---
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "Subjects",
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK,
                                ),
                                ft.Text(
                                    f"{subject1}",
                                    size=13,
                                    weight="bold",
                                    color=ft.Colors.BLUE_900,
                                ),
                                ft.Text(
                                    f"{subject2}",
                                    size=13,
                                    weight="bold",
                                    color=ft.Colors.BLUE_900,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            spacing=3,
                        ),
                        # --- Column 2: Minimum Grades ---
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "Minimum Grades",
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK,
                                ),
                                ft.Text(
                                    f"{subject1_marks}",
                                    size=13,
                                    weight="bold",
                                    color=ft.Colors.BLUE_900,
                                ),
                                ft.Text(
                                    f"{subject2_marks}",
                                    size=13,
                                    weight="bold",
                                    color=ft.Colors.BLUE_900,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            spacing=3,
                        ),
                        ft.Container(width=50),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                bgcolor="#E3EEFF",
                padding=10,
                border_radius=8,
                width=float("inf"),
            ),
            # Possible Careers Container (compact and bright)
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Possible Careers:",
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.GREEN_ACCENT_400,
                        ),
                        ft.Text(
                            f"{careers}",
                            size=13,
                            weight="bold",
                            color=ft.Colors.BLUE_900,
                        ),
                    ],
                    spacing=4,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                bgcolor="#E8F8F0",
                padding=10,
                border_radius=8,
                width=float("inf"),
            ),
        ],
        spacing=8,
            )