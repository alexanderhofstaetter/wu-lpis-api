#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, json
from WuLpisApiClass import WuLpisApi

def file_parser(filepath, separator="="):
	data = {}
	for line in open(filepath, "r"):
		line = line.rstrip('\n').split(separator)
		data[line[0]] = line[1]
	return data

if __name__ == '__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument('-a', '--action', help="Which action in the programm should run", required=True)
	parser.add_argument('-c', '--credfile', help='Path to the credentials file with username and password')
	parser.add_argument('-p', '--password')
	parser.add_argument('-u', '--username')
	parser.add_argument('-s', '--sessiondir', help='Dir where the sessions should be stored')
	parser.add_argument('-pp', '--planobject', help="Study plan object in which the correspondending course can be found (Studienplanpunkt")
	parser.add_argument('-lv', '--course', help="Course ID for which the registration should be done")
	args=parser.parse_args()

	username = file_parser(args.credfile)["username"] if args.credfile else args.username
	password = file_parser(args.credfile)["password"] if args.credfile else args.password
	
	api = WuLpisApi(username, password, args, args.sessiondir)
	method = getattr(api, args.action, None)
	if callable(method):
		method()
		print json.dumps(api.getResults(), sort_keys=True, indent=4) 