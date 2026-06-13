#!/usr/bin/python3

"""This module contains functions for retrieving data from an API"""

import requests, csv


def fetch_and_print_posts():
    try:
        res = requests.get("https://jsonplaceholder.typicode.com/posts")
        print(f"Status Code: {res.status_code}")

        if res.status_code == 200:
            data = res.json()

        for post in data:
            print(post["title"])

    except requests.RequestException as err:
        print(f"Error: {err}")


def fetch_and_save_posts():
    try:
        res = requests.get("https://jsonplaceholder.typicode.com/posts")

        if res.status_code == 200:
            data = res.json()

            posts = [
                {
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"],
                }
                for post in data
            ]

            with open(
                "posts.csv", "w", newline="", encoding="utf-8"
            ) as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(posts)

    except requests.RequestException as err:
        print(f"Error: {err}")
