CONFIG = {
	'mode':'wsgi',
	'working_dir': '/home/box/web',
	'args': (
		'--bind=0.0.0.0:8080',
		'--daemon',
		'--workers=2',
		'--temout=60',
		'hello:app',
	),
}
