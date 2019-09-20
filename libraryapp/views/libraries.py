# import sqlite3
# from django.shortcuts import render
# from libraryapp.models import Library
# from libraryapp.models import model_factory
# from ..connection import Connection
# from django.contrib.auth.decorators import login_required

# @login_required
# def list_libraries(request):
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = model_factory(Library)
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         select
#             l.id,
#             l.location_id,
#             l.user_id,
#             u.first_name,
#             u.last_name,
#             u.email
#         from libraryapp_librarian l
#         join auth_user u on l.user_id = u.id
#         """)

#         list_librarians = db_cursor.fetchall()

#     template_name = 'librarians/list.html'
#     return render(request, template_name, {'list_librarians': list_librarians})