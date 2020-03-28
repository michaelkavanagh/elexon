import argparse

from elexon import Elexon

def main():
    """Provide a simple CLI interface to the Elexon BMRS API"""
    parser = argparse.ArgumentParser(description="Query the Elexon BMRS API.")

    parser.add_argument('key', help='Elexon BMRS API Key')

    args = parser.parse_args()

    api = Elexon(args.key)

if __name__ == "__main__":
    main()
