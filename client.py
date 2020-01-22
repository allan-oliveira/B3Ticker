from b3ticker.b3ticker import B3Ticker
import string

def export_data(lpath, lst):
    with open(lpath, 'w') as f:
        for item in lst:
            f.write("%s\n" % item)

def main():
    test_set = set(string.ascii_uppercase).union(set(string.digits))
    b3ticker = B3Ticker()
    cvm_codes = b3ticker.get_cvm_codes(test_set)
    export_data('cvm_codes.txt', cvm_codes)

    b3_tickers = b3ticker.get_b3_tickers(cvm_codes)
    export_data('b3_tickers.txt', b3_tickers)

if __name__ == '__main__':
    main()