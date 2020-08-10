events_list = []

# Create event handler
def handle_keypress(event):
    print(event.char)

while True:
    if events_list == []:
        continue

    event = events_list[0]

    if event.type == 'keypress':
        handle_keypress(event)
        