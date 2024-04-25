#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

class DBStorage:
  __db = None

  def __init__(self):
      """Establishes a connection to the MySQL database."""
      try:
          self.__db = MySQLdb.connect(
              host="localhost",
              user="root",
              passwd="12345678",
              db="blogs",
              port=3306,
              charset='utf8'
          )
      except MySQLdb.Error as e:
          print(f"Error {e.args[0]}: {e.args[1]}")
          sys.exit(1)


  def all_posts(self):
      """Fetches data from the 'states' table and prints it."""
      try:
          with self.__db.cursor() as cur:
              cur.execute("SELECT * FROM posts ORDER BY id ASC")
              rows = list(cur.fetchall())

              rows_dicts = []
              for row in rows:
                  rows_dicts.append({
                      "id": row[0],
                      "title": row[1],
                      "text": row[2]
                  })

              return rows_dicts
      except MySQLdb.Error as e:
          print(f"Error {e.args[0]}: {e.args[1]}")

  def add_post(self, title, text):
      """Fetches data from the 'states' table and prints it."""
      try:
          with self.__db.cursor() as cur:
              sql = ("INSERT INTO posts(title, text) VALUES (%s, %s)")
              val = (title, text)
              cur.execute(sql, val)
              self.__db.commit()
      except MySQLdb.Error as e:
          print(f"Error {e.args[0]}: {e.args[1]}")

  def edit_post(self, id, title, text):
      """Fetches data from the 'states' table and prints it."""
      try:
          with self.__db.cursor() as cur:
              cur.execute(f"UPDATE posts SET title=\"{title}\", text=\"{text}\" WHERE id=\"{id}\"")
              self.__db.commit()
      except MySQLdb.Error as e:
          print(f"Error {e.args[0]}: {e.args[1]}")

  def delete_post(self, id):
      """Fetches data from the 'states' table and prints it."""
      try:
          with self.__db.cursor() as cur:
              cur.execute(f"DELETE FROM posts WHERE id=\"{id}\"")
              self.__db.commit()
      except MySQLdb.Error as e:
          print(f"Error {e.args[0]}: {e.args[1]}")


  def close(self):
    self.__db.close()