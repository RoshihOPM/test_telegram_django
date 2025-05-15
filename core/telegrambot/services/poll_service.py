from polls.models import PollModel
from users.models import UserProfileModel


class PollService:
    @staticmethod
    def get_next_poll_for_user(user: UserProfileModel) -> PollModel | None:
        return PollModel.objects.exclude(id__in=user.passed_polls.values_list("id", flat=True)) \
                                .order_by("created_at") \
                                .first()

    @staticmethod
    def save_user_response(poll_id: str, user: UserProfileModel, option_ids: list[int]):
        poll = PollModel.objects.filter(telegram_poll_id=poll_id).first()
        if poll:
            poll.user_options = option_ids
            poll.save()

            user.passed_polls.add(poll)
            user.completed_polls += 1
            user.save()

    @staticmethod
    def save_poll_answer(poll_id: str, user, option_ids: list[int]):
        poll = PollModel.objects.get(telegram_poll_id=poll_id)
        poll.user_options = option_ids
        poll.save()

        user.passed_polls.add(poll)
