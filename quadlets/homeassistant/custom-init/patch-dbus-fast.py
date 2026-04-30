#!/usr/bin/env sh
sed -i -e '/uid: int \| None = None/ s/= None/= UID_NOT_SPECIFIED/' /usr/local/lib/python3.14/site-packages/dbus_fast/auth.py
