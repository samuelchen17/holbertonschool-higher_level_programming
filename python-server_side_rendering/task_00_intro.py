import os


def generate_invitations(template, attendees):
    """Generate invitation from template"""

    # check type
    if not isinstance(template, str):
        print(f"template not str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        print(f"attendees not list, got {type(attendees).__name__}.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("attendees not list of dicts")
        return

    # check if empty
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invite = template

        variables = {
            "name": attendee.get("name"),
            "event_title": attendee.get("event_title"),
            "event_date": attendee.get("event_date"),
            "event_location": attendee.get("event_location"),
        }

        for key, value in variables.items():
            if value is None:
                value = "N/A"

            invite = invite.replace(f"{{{key}}}", str(value))

        filename = f"output_{index}.txt"

        if os.path.exists(filename):
            print(f"{filename} already exists.")

        try:
            if os.path.exists(filename):
                print(f"{filename} already exists.")

            with open(filename, "w") as file:
                file.write(invite)

        except OSError as err:
            print(f"Error {filename}: {err}")
