<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  </head>
  <body>
    % if message and len(message)>1:
    <span>{{message}}
    % end
    <div class="table-responsive">        
      <table class="table">
	<thead>
	  <th>Device</th>
	  <th>State</th>
	  <th>Action</th>
	</thead>
	<tbody>
	  <tr>
            <td>Left</td>
            <td><span class="label {{lclass}}">{{lstate}}</span></td>
            <td>
	      <a class="btn btn-primary" href="/pulse/{{lchan}}" role="button">Pulse</a>
	    </td>
	  </tr>
	  <tr>
            <td>Right</td>
            <td><span class="label {{rclass}}">{{rstate}}</span></td>
            <td>
	      <a class="btn btn-primary" href="/pulse/{{rchan}}" role="button">Pulse</a>
	    </td>
	  </tr>
	</tbody>
      </table>
    </div>
  </body>
</html>

