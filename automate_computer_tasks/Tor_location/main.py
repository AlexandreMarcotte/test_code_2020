from find_tor_ip_and_save_as_html import pull_html_from_ip_adress_site_on_tor
from parse_html_for_info import find_ip_address


def main():
    for _ in range(1):
        pull_html_from_ip_adress_site_on_tor()
        print(find_ip_address())


if __name__ == '__main__':
    main()
