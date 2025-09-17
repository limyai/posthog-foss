# ruff: noqa: T201 allow print statements

from django.core.management.base import BaseCommand

from posthog.models import PersonalAPIKey, User
from posthog.models.personal_api_key import hash_key_value
from posthog.models.utils import generate_random_token


class Command(BaseCommand):
    help = "Create a personal API key for a user"

    def add_arguments(self, parser):
        parser.add_argument(
            "--email",
            type=str,
            required=True,
            help="Email of the user to create the API key for",
        )
        parser.add_argument(
            "--label",
            type=str,
            default="CLI Generated Key",
            help="Label for the API key (default: 'CLI Generated Key')",
        )
        parser.add_argument(
            "--key",
            type=str,
            help="Custom API key value (if not provided, one will be generated)",
        )

    def handle(self, *args, **options):
        email = options["email"]
        label = options["label"]
        custom_key = options["key"]

        # Find the user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User with email '{email}' does not exist!"))
            return

        # Generate or use provided key
        if custom_key:
            api_key_value = custom_key
        else:
            api_key_value = generate_random_token()

        # Create the API key
        try:
            personal_api_key = PersonalAPIKey.objects.create(
                user=user,
                label=label,
                secure_value=hash_key_value(api_key_value),
            )

            self.stdout.write(self.style.SUCCESS(f"✅ Successfully created personal API key!"))
            self.stdout.write(f"User: {user.email}")
            self.stdout.write(f"Label: {label}")
            self.stdout.write(f"API Key: {api_key_value}")
            self.stdout.write(f"Key ID: {personal_api_key.id}")
            self.stdout.write(self.style.WARNING("⚠️  Save this API key - it won't be shown again!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to create API key: {str(e)}"))
