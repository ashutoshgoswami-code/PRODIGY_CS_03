# ============================================================
# PRODIGY INFOTECH - Cyber Security Internship
# Task-03: Password Complexity Checker
# Author: Ashutosh Goswami
# ============================================================

import re


def check_password_strength(password):
    """
    Analyzes password strength based on multiple criteria.
    Returns a score, strength label, and detailed feedback.
    """
    score = 0
    feedback = []

    # ── Criterion 1: Length ──────────────────────────────────
    length = len(password)
    if length >= 16:
        score += 3
        feedback.append("✅ Excellent length (16+ characters)")
    elif length >= 12:
        score += 2
        feedback.append("✅ Good length (12-15 characters)")
    elif length >= 8:
        score += 1
        feedback.append("⚠️  Minimum length met (8-11 characters)")
    else:
        feedback.append("❌ Too short (minimum 8 characters recommended)")

    # ── Criterion 2: Uppercase Letters ──────────────────────
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ No uppercase letters (add A-Z)")

    # ── Criterion 3: Lowercase Letters ──────────────────────
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ No lowercase letters (add a-z)")

    # ── Criterion 4: Numbers ────────────────────────────────
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ No numbers (add 0-9)")

    # ── Criterion 5: Special Characters ─────────────────────
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/~`]', password):
        score += 2
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ No special characters (add !@#$% etc.)")

    # ── Criterion 6: No Common Patterns ─────────────────────
    common_patterns = ['123456', 'password', 'qwerty', 'abc123',
                       '111111', 'letmein', 'welcome', '000000']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        feedback.append("❌ Contains common pattern (very weak!)")
    else:
        feedback.append("✅ No common patterns detected")

    # ── Strength Label ───────────────────────────────────────
    if score >= 7:
        strength = "🟢 VERY STRONG"
    elif score >= 5:
        strength = "🟡 STRONG"
    elif score >= 3:
        strength = "🟠 MODERATE"
    elif score >= 1:
        strength = "🔴 WEAK"
    else:
        strength = "⛔ VERY WEAK"

    return score, strength, feedback


def get_strength_bar(score):
    """Returns a visual progress bar based on score."""
    max_score = 8
    filled = min(score, max_score)
    bar = "█" * filled + "░" * (max_score - filled)
    return f"[{bar}] {filled}/{max_score}"


def main():
    print("=" * 55)
    print("  PASSWORD COMPLEXITY CHECKER - Prodigy InfoTech Task-03")
    print("=" * 55)

    while True:
        print("\nOptions:")
        print("  1. Check password strength")
        print("  2. Exit")

        choice = input("\nEnter your choice (1/2): ").strip()

        if choice == '1':
            password = input("\nEnter password to check: ")

            score, strength, feedback = check_password_strength(password)

            print("\n" + "-" * 45)
            print(f"  Strength : {strength}")
            print(f"  Score    : {get_strength_bar(score)}")
            print("-" * 45)
            print("  Detailed Feedback:")
            for item in feedback:
                print(f"    {item}")
            print("-" * 45)

        elif choice == '2':
            print("\n  Exiting Password Checker. Goodbye!")
            break

        else:
            print("  [!] Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    main()
