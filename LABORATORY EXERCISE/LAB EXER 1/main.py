# IT Automation Incident Ticket Manager
# Linear Data Structure Implementation (List / Dynamic Array)

# Pre-populated list with the 10 required sample incident tickets
incident_tickets = [
    {"id": "INC1392939", "bot": "BOT-Inventory", "desc": "Failed to generate the daily report"},
    {"id": "INC1392940", "bot": "BOT-Email", "desc": "Failed to send the scheduled notification"},
    {"id": "INC1392941", "bot": "BOT-DataSync", "desc": "Encountered an error during data transfer"},
    {"id": "INC1392942", "bot": "BOT-Invoice", "desc": "Failed to process an invoice"},
    {"id": "INC1392943", "bot": "BOT-Report", "desc": "Failed to generate the weekly report"},
    {"id": "INC1392944", "bot": "BOT-FileTransfer", "desc": "Failed to upload the required file"},
    {"id": "INC1392945", "bot": "BOT-DataEntry", "desc": "Encountered an error while entering records"},
    {"id": "INC1392946", "bot": "BOT-Backup", "desc": "Failed to complete the scheduled backup"},
    {"id": "INC1392947", "bot": "BOT-Validation", "desc": "Failed to validate the submitted records"},
    {"id": "INC1392948", "bot": "BOT-Notification", "desc": "Failed to send the system alert"}
]

def add_ticket():
    print("\n--- Add New Incident Ticket ---")
    ticket_id = input("Enter Incident ID: ").strip()
    
    # Check for duplicate ID
    for ticket in incident_tickets:
        if ticket["id"].lower() == ticket_id.lower():
            print(f"[!] Error: Incident ID '{ticket_id}' already exists.")
            return

    bot = input("Enter Bot Name: ").strip()
    desc = input("Enter Short Description: ").strip()

    if not ticket_id or not bot or not desc:
        print("[!] Error: All fields are required.")
        return

    incident_tickets.append({
        "id": ticket_id,
        "bot": bot,
        "desc": desc
    })
    print(f"[+] Incident ticket '{ticket_id}' successfully added.")

def display_tickets():
    print("\n========================= ACTIVE INCIDENT TICKETS =========================")
    if not incident_tickets:
        print("No active incident tickets found.")
        print("==========================================================================")
        return

    print(f"{'Incident ID':<15} | {'Bot Name':<20} | {'Short Description'}")
    print("-" * 75)
    for ticket in incident_tickets:
        print(f"{ticket['id']:<15} | {ticket['bot']:<20} | {ticket['desc']}")
    print("==========================================================================")

def search_ticket():
    print("\n--- Search Incident Ticket ---")
    search_id = input("Enter Incident ID to search: ").strip()
    
    for ticket in incident_tickets:
        if ticket["id"].lower() == search_id.lower():
            print("\n[✓] Ticket Found:")
            print(f"  Incident ID       : {ticket['id']}")
            print(f"  Bot Name          : {ticket['bot']}")
            print(f"  Short Description : {ticket['desc']}")
            return

    print(f"[!] Incident ticket with ID '{search_id}' not found.")

def remove_ticket():
    print("\n--- Remove Resolved Incident Ticket ---")
    remove_id = input("Enter Incident ID of the resolved ticket: ").strip()
    
    for index, ticket in enumerate(incident_tickets):
        if ticket["id"].lower() == remove_id.lower():
            removed = incident_tickets.pop(index)
            print(f"[✓] Resolved ticket '{removed['id']}' ({removed['bot']}) removed successfully.")
            return

    print(f"[!] Incident ticket with ID '{remove_id}' not found.")

def display_count():
    print("\n--- Total Active Incident Tickets ---")
    total = len(incident_tickets)
    print(f"Total Active Tickets: {total}")

def main():
    while True:
        print("\n==============================================")
        print("   IT AUTOMATION INCIDENT TICKET MANAGER      ")
        print("==============================================")
        print("1. Add a New Incident Ticket")
        print("2. Display All Active Incident Tickets")
        print("3. Search for a Specific Incident Ticket")
        print("4. Remove a Resolved Incident Ticket")
        print("5. Display Total Number of Active Tickets")
        print("6. Exit")
        print("==============================================")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_ticket()
        elif choice == '2':
            display_tickets()
        elif choice == '3':
            search_ticket()
        elif choice == '4':
            remove_ticket()
        elif choice == '5':
            display_count()
        elif choice == '6':
            print("\nExiting IT Automation Incident Ticket Manager. Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
