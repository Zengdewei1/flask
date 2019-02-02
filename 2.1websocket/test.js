var s = new WebSocket("%s://%s/foobar/");
s.onopen = function() {}
s.onmessage = function(e) {}
s.onerror = function(e) {}
s.onclose = function(e) {}
s.send(value);