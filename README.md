# Bridge Forwarding Table Simulator

![flowchart of bridge decisions](NBMetadataCache.jpeg)

This program simulates the a bridge learning algorithm. It demonstrates how a network bridge learn and updates it's Forwarding Database (FDB) based on observed frames and determines whether to forward, discard or broadcast frames.

The simulation processes two input files:

- Bridge FDB text: contains initial forwarding database (mac to port mapping)
- Randome Frames text: contains randomly generated frames with source mac, dest mac, and arrival port.

The program outputs:

- Output text file. showing the bridge's forwarding decision for each frame.
- Updated Bridge FDB text: reflecting any new or moved mac entries.

## How it works

1. Read BridgeFDB.txt : load initial database into a dictionary (mac -> port)
2. Read RandomFrames.txt : read every 3 line frame: souce mac, dest mac and arrival port.
3. Apply bridge algo :

- if the source mac is not in FDB, add with observed port.
- if source mac exists but is on a different port, update it to new port.
- then check destination mac: if it's found on a different port, forward the frame to that port. if it's found but on the same port, discard the frame. if it's not found, broadcast the frame.

4. Output to Output.txt in the format of : <sourceMAC> <destinationMAC> <ArrivalPort> <Action>

## How to Run

- Prerequisites: Python 3.x
- Run the program:
  `python3 learning_bridge.py`

## License

This project's code was release under the MIT license. Full documentation resources can be found at their [website](https://opensource.org/license/MIT).
