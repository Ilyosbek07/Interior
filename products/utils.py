def get_card_lengs(request):
	return len(request.session.get('card', []))

