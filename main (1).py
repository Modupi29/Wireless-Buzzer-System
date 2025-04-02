import socket

host = "255.255.255.255"
port = 5005
buffer_size = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(0.1)

while True:
    command = input("Enter command (ACTIVATE/DEACTIVATE or EXIT to quit): ").strip().upper()
    
    if command == "EXIT":
        print("Exiting client...")
        break
    
    elif command == "ACTIVATE":
        print("Sending command: ACTIVATE")
        message = "ACTIVATE"
    
    elif command == "DEACTIVATE":
        print("Sending command: DEACTIVATE")
        message = "DEACTIVATE"
    
    else:
        print("Invalid command... Please enter 'ACTIVATE' or 'DEACTIVATE'.")
        continue

    try:
        client.sendto(message.encode(), (host, port))
        response, _ = client.recvfrom(buffer_size)
        print(f"Receiving  response: {response.decode()}")
        
    except socket.timeout:
        print("The connection timed out")
    
    except Exception as e:  
        print(f"An error occurred: {e}")

print("Closing the connection...")
client.close() 

