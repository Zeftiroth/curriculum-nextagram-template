{ % if current_user.is_following(i) % }
{% else%}
<div > </div >

{% endif%}


<link
      rel = "icon"
      href = "{{url_for('static', filename='images/next16x16.png')}}"
      type = "image/png"
    />
