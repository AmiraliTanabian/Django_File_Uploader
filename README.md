This project doesn't serve any particular purpose and was created for practice. It allows you to easily upload a file, store it, and view it in the Django admin panel.

## How to use
<ul>
  <li>
    Clone the repository 
  </li>

  ```
git clone https://github.com/AmiraliTanabian/Django_File_Uploader.git && cd Django_File_Uploader
```

  <li>
    Install Django
  </li>

``` 
pip install django
```
<li>
  Set up the database
</li>

```
python3 manage.py migrate
```

<li>
  Create a user to access the admin panel
</li>

```
python3 manage.py migrate
```

<li>
  Run it on localhost
</li>

```
python3 manage.py runsever
```

Go to http://localhost:8000

<b>Note1:</b>
Please note that to view the files, go to the <b>media</b> folder. This path can be changed via ```MEDIA_ROOT``` in the <b>settings.py</b> file.

<b>Note2:</b>
In Windows, instead of using all nstances of <b>python3</b> , use <b>python</b>.

Thank you for your attention.
</ul>
