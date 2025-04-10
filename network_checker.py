import subprocess
import platform
import logging
import argparse
from datetime import datetime
from pathlib import Path

class NetworkChecker:
    def __init__(self, hosts, log_file="network_status.log"):
        self.hosts = hosts
        self.log_file = Path(log_file)
        self.os_type = platform.system()
        self.setup_logger()

    def setup_logger(self):
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        logging.info("Network Connectivity Check Initialized")

    def ping_host(self, host):
        try:
            param = "-n" if self.os_type == "Windows" else "-c"
            command = ["ping", param, "1", host]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                status = "Online"
                logging.info(f"{host} is {status}")
            else:
                status = "Offline"
                logging.warning(f"{host} is {status}")
            return host, status
        except Exception as e:
            logging.error(f"Error pinging {host}: {e}")
            return host, "Error"

    def run_check(self):
        print(f"📡 Network Connectivity Checker — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)
        for host in self.hosts:
            host, status = self.ping_host(host)
            status_icon = "✅" if status == "Online" else "❌"
            print(f"{status_icon} {host}: {status}")
        print("=" * 50)
        print(f"Logs saved to: {self.log_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Connectivity Checker")
    parser.add_argument(
        "--hosts", "-H", nargs="+", required=True,
        help="List of hostnames or IP addresses to check"
    )
    parser.add_argument(
        "--log", "-l", default="network_status.log",
        help="Log file to store status"
    )

    args = parser.parse_args()
    checker = NetworkChecker(args.hosts, args.log)
    checker.run_check()
