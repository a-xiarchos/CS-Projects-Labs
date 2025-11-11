# CS-Projects-Labs

Sandbox for tracking computer-science labs and personal practice projects.

## Structure
- `Labs/`: coursework-style exercises and lab notes.
- `Projects/`: longer-form experiments or prototypes spun off from lab work.

### Current Highlight
- [`Projects/network_scanner`](Projects/network_scanner): Python (`python-nmap`) utility that discovers hosts on a CIDR block and optionally enumerates open ports. Requirements and usage examples live in that folder’s README; quick start:
  ```bash
  cd Projects/network_scanner
  python3 network_scan.py 192.168.2.0/24 --top-ports 100
  ```

## Getting Started
```bash
git clone https://github.com/anthonyxiarchos1997-debug/CS-Projects-Labs.git
cd CS-Projects-Labs
```
Create subfolders under `Labs/` or `Projects/` as you add new work, then commit and push normally.
