import datetime
import uuid

token = jwt.encode(
	{
		"iss": "6d1102ab-1b5e-4b80-92e4-fdcb8a03a50c",
		"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
		"jti": str(uuid.uuid4()),
		"aud": "tableau",
		"sub": "jmi2124@columbia.edu",
		"scp": "tableau:views:embed"
	},
		'un5V/bZTyhbuHiD/xm8MdGLGK+rr9fCyY0s0jrJtPss=',
		algorithm = "HS256",
		headers = {
		'kid': "77ef5686-b138-4468-92ff-b257e3fac198",
		'iss': "6d1102ab-1b5e-4b80-92e4-fdcb8a03a50c"
        }
  )