#!/usr/bin/env python3
"""
Password Generator - Simple CLI Version
"""
import secrets
import string

class PasswordGenerator:
    DIGITS = string.digits
    UPPERCASE = string.ascii_uppercase
    LOWERCASE = string.ascii_lowercase
    SPECIAL = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    def generate(self, length, use_digits=True, use_uppercase=True, use_lowercase=True, use_special=False):
        chars = ''
        if use_digits: chars += self.DIGITS
        if use_uppercase: chars += self.UPPERCASE
        if use_lowercase: chars += self.LOWERCASE
        if use_special: chars += self.SPECIAL
        if not chars: chars = self.LOWERCASE
        return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == '__main__':
    gen = PasswordGenerator()
    print("Password:", gen.generate(16))
