from dora import Node
import pyarrow as pa

def main():
    node = Node()

    action = None
    for event in node:
        if event["type"] == "INPUT":
            event_id = event["id"]
            if event_id == "action":
                action = event["value"].to_pylist()
                node.send_output("action", pa.array(action), metadata={})
            # elif event_id == "tick":
            #     if action is not None:
            #         node.send_output("action", pa.array(action), metadata={})

if __name__ == "__main__":
    main()