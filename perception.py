from dora import Node
import pyarrow as pa

def main():
    node = Node()

    raw_data = None
    for event in node:
        if event["type"] == "INPUT":
            event_id = event["id"]
            if event_id == "raw_data":
                raw_data = event["value"].to_pylist()
                node.send_output("raw_data", pa.array(raw_data), metadata={})
            # elif event_id == "tick":
            #     if raw_data is not None:
            #         node.send_output("raw_data", pa.array(raw_data), metadata={})

if __name__ == "__main__":
    main()