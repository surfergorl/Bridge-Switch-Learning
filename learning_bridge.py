dictionary = {}

def split_frames():
    output_file = open('output.txt', 'w')
        
    try:
        with open('RandomFrames.txt', 'r') as file: 
            content = file.readlines()
            for i in range(0, len(content), 3):
                source_mac = content[i].strip()
                dest_mac = content[i+1].strip()
                source_port = content[i+2].strip()
                
                port_of_sender = dictionary.get(source_mac, 'not found')

                if port_of_sender == 'not found' or port_of_sender != source_port: 
                    dictionary[source_mac] = source_port 

                port_of_destination = dictionary.get(dest_mac, 'not found')
                port_of_sender = dictionary.get(source_mac, 'not found')


                if port_of_destination == 'not found': 
                    action = 'Broadcast'
                if port_of_destination == source_port: 
                    action = 'Discard'
                if port_of_destination != source_port and port_of_destination != 'not found': 
                    action = f'Forward on port {port_of_destination}'

                print(f'{source_mac:<20} {dest_mac:<20} {source_port:<5} {action}', file=output_file)


    except FileExistsError:
        print('File not found')
    except Exception as e: 
        print(f'An unexpected error occured: {e}')


def make_map():
    global dictionary
    try:
        with open('BridgeFDB.txt', 'r') as file: 
            lines = file.readlines()
            for i in range (0, len(lines), 2): 
                mac = lines[i].strip()
                port = lines[i+1].strip()
                dictionary[mac] = port
                
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error occurred: {e}')


def main():
    make_map()
    split_frames()

if __name__ == "__main__":
    main()