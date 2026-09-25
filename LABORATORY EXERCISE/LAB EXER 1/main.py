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

BOX_WIDTH = 58

def print_box(text, align="left"):
    """Utility to print perfectly aligned single-line message boxes."""
    inner_width = BOX_WIDTH - 2
    if align == "center":
        content = text.center(inner_width)
    else:
        content = f" {text}".ljust(inner_width)
        
    print(f"\n┌{'─' * inner_width}┐")
    print(f"│{content}│")
    print(f"└{'─' * inner_width}┘")

def add_ticket():
    print_box("CREATE NEW INCIDENT TICKET", align="center")
    ticket_id = input("  » Incident ID       : ").strip()
    
    # Check for duplicate ID
    for ticket in incident_tickets:
        if ticket["id"].lower() == ticket_id.lower():
            print_box(f"[!] REJECTED: ID '{ticket_id}' already exists!")
            return

    bot = input("  » Bot Identifier    : ").strip()
    desc = input("  » Brief Description : ").strip()

    if not ticket_id or not bot or not desc:
        print_box("[!] REJECTED: All record attributes are mandatory!")
        return

    incident_tickets.append({
        "id": ticket_id,
        "bot": bot,
        "desc": desc
    })
    print_box(f"[+] SUCCESS: Ticket '{ticket_id}' added to queue!")

def display_tickets():
    print("\n┌─────────────────────────────────────────────────────────────────────────────────────────┐")
    print("│                            CURRENT ACTIVE INCIDENT REGISTRY                             │")
    print("├─────────────────┬───────────────────────┬───────────────────────────────────────────────┤")
    print("│ INCIDENT ID     │ BOT SOURCE            │ LOGGED ISSUE DESCRIPTION                      │")
    print("├─────────────────┼───────────────────────┼───────────────────────────────────────────────┤")
    
    if not incident_tickets:
        print("│                        No active incident tickets found.                                │")
        print("└─────────────────┴───────────────────────┴───────────────────────────────────────────────┘")
        return

    for ticket in incident_tickets:
        print(f"│ {ticket['id']:<15} │ {ticket['bot']:<21} │ {ticket['desc']:<45} │")
        print("├─────────────────┼───────────────────────┼───────────────────────────────────────────────┤")
        
    print("└─────────────────┴───────────────────────┴───────────────────────────────────────────────┘")

def search_ticket():
    print_box("REGISTRY QUERY ENGINE", align="center")
    search_id = input("  » Enter Target Incident ID: ").strip()
    
    for ticket in incident_tickets:
        if ticket["id"].lower() == search_id.lower():
            print("\n┌────────────────────────────────────────────────────────┐")
            print("│                  TICKET RECORD FOUND                   │")
            print("├─────────────────┬──────────────────────────────────────┤")
            print(f"│ Incident ID     │ {ticket['id']:<36} │")
            print("├─────────────────┼──────────────────────────────────────┤")
            print(f"│ Source Bot      │ {ticket['bot']:<36} │")
            print("├─────────────────┼──────────────────────────────────────┤")
            print(f"│ Description     │ {ticket['desc']:<36} │")
            print("└─────────────────┴──────────────────────────────────────┘")
            return

    print_box(f"[!] NOT FOUND: No match discovered for '{search_id}'!")

def remove_ticket():
    print_box("RESOLVE & REMOVE INCIDENT", align="center")
    remove_id = input("  » Enter Resolved Incident ID: ").strip()
    
    for index, ticket in enumerate(incident_tickets):
        if ticket["id"].lower() == remove_id.lower():
            removed = incident_tickets.pop(index)
            print_box(f"[+] RESOLVED: Ticket '{removed['id']}' purged!")
            return

    print_box(f"[!] NOT FOUND: No record found with ID '{remove_id}'!")

def display_count():
    total = len(incident_tickets)
    print_box(f"TOTAL ACTIVE INCIDENTS IN QUEUE: {total}")

def main():
    while True:
        print("\n┌────────────────────────────────────────────────────────┐")
        print("│       IT AUTOMATION INCIDENT TICKET MANAGER            │")
        print("│         Central Monitoring & Operations Hub            │")
        print("├────────────────────────────────────────────────────────┤")
        print("│  [1] Register New Incident Ticket                      │")
        print("│  [2] Display All Active Incidents                      │")
        print("│  [3] Search Record by Incident ID                      │")
        print("│  [4] Resolve & Remove Incident                         │")
        print("│  [5] View Active Incident Metrics                      │")
        print("│  [6] Terminate Console Session                         │")
        print("└────────────────────────────────────────────────────────┘")
        
        choice = input("  Select Operation [1-6]: ").strip()
        
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
            print_box("Session closed. System offline. Goodbye!", align="center")
            break
        else:
            print_box("[!] Invalid selection! Please enter 1 to 6.")

if __name__ == "__main__":
    main()
