# COMPLETED BY 
# /////////////////////////////////////////////
# ANURAG DAS
# STUDENT ID 126031228
# EMAIL- adas35@myseneca.ca
# /////////////////////////////////////////////

This repository showcases a basic Python client-server application, illustrating fundamental networking concepts through sockets and leveraging multi-threading for concurrent client handling.

## SYNOPSIS

The suite comprises two primary components:

`client.py`: Embodies the client-side functionality, establishing a server connection, transmitting messages, and showcasing server replies.

`server.py`: Operates as the server, awaiting client connections, reverberating received messages, and employing threads to manage multiple connections concurrently.

### SERVER USAGE

Initiate the server with:

```bash
python server.py
```

Upon execution, the server commences on `localhost` (127.0.0.1), binding to port 27000, ready to accept client connections.

### CLIENT INTERACTION

To link a client with the server:

```bash
python client.py
```

Executing the client script prompts for message input. Upon submission, the server echoes the message. Exiting requires an `exit` command.

## TECHNICAL INSIGHTS

### Server Framework

- Operates on port `27000`, accommodating up to five simultaneous client engagements.
- Individual threads are spun for each client, facilitating message echo functionalities.

### Client Mechanics

- Establishes a connection to  `127.0.0.1:27000`.
- Enables message sending to the server, displaying the echoed response.
- Terminates upon `exit` command entry by the user.
