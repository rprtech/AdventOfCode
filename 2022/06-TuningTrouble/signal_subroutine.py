import sys
import itertools

class Signal:
    def _contains_duplicate(self, sig_list: list) -> bool:
        for x,y in itertools.combinations(sig_list, 2):
            if x == y: return True

        return False
    

    def _find_start_marker(self, length: int) -> int:
        compare_num_prev_chars: int = length - 1
        start_loc: int = 0

        for char_count, char in enumerate(self.buffer, start = 1):
            end_loc = start_loc + compare_num_prev_chars
            if char_count <= compare_num_prev_chars: continue
            
            if self._contains_duplicate(self.buffer[start_loc:end_loc]):
                start_loc += 1
                continue

            if char not in self.buffer[start_loc:end_loc]:
                return char_count
            else:
                start_loc += 1


    def __init__(self, buffer: str, pkt_length: int = 4, msg_length: int = 14) -> None:
        self.buffer = tuple(buffer)
        self.pkt_length: int = pkt_length
        self.pkt_start_location: int = self._find_start_marker(self.pkt_length)
        self.pkt_marker = self.buffer[self.pkt_start_location - self.pkt_length : self.pkt_start_location]
        self.msg_length: int = msg_length
        self.msg_start_location: int = self._find_start_marker(self.msg_length)
        self.msg_marker = self.buffer[self.msg_start_location - self.msg_length : self.msg_start_location]

        
        #self._find_start_marker()

def main() -> None:
    if len(sys.argv) < 2:
        raise RuntimeError('ERROR: Missing input file')

    with open(sys.argv[1], 'r') as f:
        elf_signal = Signal(f.readline())
    
    print(f'Packet Start Location = {elf_signal.pkt_start_location} \nPacket Marker = {"".join(map(str, elf_signal.pkt_marker))}')
    print(f'Message Start Location = {elf_signal.msg_start_location} \nMessage Marker = {"".join(map(str, elf_signal.msg_marker))}')



### Call Main ###
if __name__ == '__main__':
    main()