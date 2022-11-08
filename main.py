from blockchain import Blockchain
import json

def main():
    blockchain = Blockchain()

    t1 = blockchain.new_data("Tommy Siuuuuuu", "Tommy Scherphorn", "5", "BTC")
    t2 = blockchain.new_data("JP", "Andre", "0.5", "BTC")
    t3 = blockchain.new_data("Dr. Bayntun", "Patrick", "1000", "BTC")
    blockchain.add_block(12)

    t4 = blockchain.new_data("Joe", "Ma", "10", "BTC")
    t5 = blockchain.new_data("Updog", "under there", "0.1", "BTC")
    t6 = blockchain.new_data("Barrack", "Obama", "2000", "BTC")
    blockchain.add_block(15)

    print("Blockchain:")
    print(*blockchain.chain, sep = "\n\n")
    print("\n")
    print(blockchain.is_valid(blockchain.chain))

if __name__ == "__main__":
    main()