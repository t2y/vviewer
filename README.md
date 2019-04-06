# vviewer

text viewer to show row data vertically

## How to install

from pypi

```bash
(vviewer) $ pip install vviewer
```

for development

```bash
(vviewer) $ python setup.py develop
```

## How to use

```bash
(vviewer) $ vviewer -h
usage: vviewer [-h] [-c [COLUMN [COLUMN ...]]] [-d DELIMITER] [-e ENCODING]
               [--header HEADER] [--quotechar QUOTECHAR] [--quoting QUOTING]
               [--sort]
               data

positional arguments:
  data                  set path to data file

optional arguments:
  -h, --help            show this help message and exit
  -c [COLUMN [COLUMN ...]], --column [COLUMN [COLUMN ...]]
                        set column to display
  -d DELIMITER, --delimiter DELIMITER
                        set delimiter character in file
  -e ENCODING, --encoding ENCODING
                        set encoding
  --header HEADER       set path to header file
  --quotechar QUOTECHAR
                        set quote character in file
  --quoting QUOTING     set quoting
  --sort                sort row data with header column name
```

### Show all columns 

```bash
(vviewer) $ vviewer tests/fixtures/blocks.csv

##### line no: 1
------------------------------------------------------------------------
001: number           : 100
002: hash             : 0xb40a0dfde1b270d7c58c3cb505c7e773c50198b28cce3e442c4e2f33ff764582
003: parent_hash      : 0x3dd4dc843801af12c0a6dd687642467a3ce835dca09159734dec03109a1c1f1f
004: nonce            : 0x6d88b33209e0a320
005: sha3_uncles      : 0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347
006: logs_bloom       : 0x0000000000000000000000000000000000000000000000000...(snip)
007: transactions_root: 0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421
008: state_root       : 0xf5f18c33ddff06efa928d22a2432fb34a11e6f62cce825cdad1c78e1068e6b7b
009: receipts_root    : 0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421
010: miner            : 0xc2fa6dcef5a1fbf70028c5636e7f64cd46e7cfd4
011: difficulty       : 827755
012: total_difficulty : 85797483
013: size             : 535
014: extra_data       : 0xd783010502846765746887676f312e362e33856c696e7578
015: gas_limit        : 15217318
016: gas_used         : 0
017: timestamp        : 1479653850
018: transaction_count: 0
------------------------------------------------------------------------
Enter to next line, or q (quit):
```

### Filter any columns

```bash
(vviewer) $ vviewer tests/fixtures/blocks.csv -c number hash nonce miner

##### line no: 1
------------------------------------------------------------------------
001: number           : 100
002: hash             : 0xb40a0dfde1b270d7c58c3cb505c7e773c50198b28cce3e442c4e2f33ff764582
004: nonce            : 0x6d88b33209e0a320
010: miner            : 0xc2fa6dcef5a1fbf70028c5636e7f64cd46e7cfd4
------------------------------------------------------------------------
Enter to next line, or q (quit):
```

### Use header.txt when data does not have the header line

```bash
(vviewer) $ vviewer tests/fixtures/blocks_without_header.csv --header tests/fixtures/blocks_header.txt

##### line no: 1
------------------------------------------------------------------------
001: number           : 100
002: hash             : 0xb40a0dfde1b270d7c58c3cb505c7e773c50198b28cce3e442c4e2f33ff764582
003: parent_hash      : 0x3dd4dc843801af12c0a6dd687642467a3ce835dca09159734dec03109a1c1f1f
004: nonce            : 0x6d88b33209e0a320
005: sha3_uncles      : 0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347
006: logs_bloom       : 0x0000000000000000000000000000000000000000000000000...(snip)
007: transactions_root: 0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421
008: state_root       : 0xf5f18c33ddff06efa928d22a2432fb34a11e6f62cce825cdad1c78e1068e6b7b
009: receipts_root    : 0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421
010: miner            : 0xc2fa6dcef5a1fbf70028c5636e7f64cd46e7cfd4
011: difficulty       : 827755
012: total_difficulty : 85797483
013: size             : 535
014: extra_data       : 0xd783010502846765746887676f312e362e33856c696e7578
015: gas_limit        : 15217318
016: gas_used         : 0
017: timestamp        : 1479653850
018: transaction_count: 0
------------------------------------------------------------------------
Enter to next line, or q (quit):
```

### Complex example including east asian characters

```bash
(vviewer-public) $ vviewer tests/fixtures/e-stat-10102.csv --quoting all --column "調査年 コード" "B1106_森林面積【ｈａ】" "B2101_自然公園面積【ｈａ】" "B4110_最深積雪【ｃｍ】"

##### line no: 1
------------------------------------------------------------------------
001: 調査年 コード                                 : 2016100000
011: B1106_森林面積【ｈａ】                        : ***
023: B2101_自然公園面積【ｈａ】                    : 5,565,967.00
047: B4110_最深積雪【ｃｍ】                        : ***
------------------------------------------------------------------------
Enter to next line, or q (quit):
```
