# ip-parsing

Student: Sanzhar Nakyp

This program splits ip into first, last and broadcast addresses

## Usage

```bash
python3 main.py
```

## Examples
### 1st example

Input:

```
>>> Enter ip address: 1.53.165.233
>>> Enter mask: 23
```

Output:

```
First address: 00000001.00110101.10100100.00000001 => 1.53.164.1
Last address: 00000001.00110101.10100101.11111110 => 1.53.165.254
Broadcast address: 00000001.00110101.10100101.11111111 => 1.53.165.255
```

### 2nd example

Input:

```
>>> Enter ip address: 203.206.46.58
>>> Enter mask: 23
```

Output:

```
First address: 11001011.11001110.00101110.00000001 => 203.206.46.1
Last address: 11001011.11001110.00101111.11111110 => 203.206.47.254
Broadcast address: 11001011.11001110.00101111.11111111 => 203.206.47.255
```

### 3rd example

Input:

```
>>> Enter ip address: 221.75.50.14
>>> Enter mask: 18
```

Output:

```
First address: 11011101.01001011.00000000.00000001 => 221.75.0.1
Last address: 11011101.01001011.00111111.11111110 => 221.75.63.254
Broadcast address: 11011101.01001011.00111111.11111111 => 221.75.63.255
```
