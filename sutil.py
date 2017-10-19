#!/usr/bin/env python3
"""
Some simple utils to make working with snaps and the snap store APIs
a bit more convenient.
"""

import argparse
import requests


def main():
    parser = argparse.ArgumentParser(
        description='Snap Utils'
    )

    parser.add_argument('-v', '--debug', action='store_true')
    parser.add_argument('-i', '--id', action='store_true')
    parser.add_argument('-n', '--name', action='store_true')
    parser.add_argument('val', nargs='?')
    args = parser.parse_args()

    if args.id:
        res = requests.get('https://api.snapcraft.io/api/v1/snaps/details/%s' % args.val,
                           headers={'X-Ubuntu-Series': '16'})
        if res.status_code == 200:
            print(res.json()['snap_id'])
        else:
            print('Snap %s not found' % args.val)
    elif args.name:
        res = requests.get('https://assertions.ubuntu.com/v1/assertions/snap-declaration/16/%s' % args.val)
        if res.status_code == 200:
            print(res.json()['headers']['snap-name'])
        else:
            print('Snap id %s not found' % args.val)

if __name__ == '__main__':
    main()
