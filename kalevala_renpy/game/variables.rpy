## Game Variables and State Management

# Default starting values
default silver = 150
default inventory = []
default titles = []
default financial_wisdom = 0
default decisions = []

# Companion approval (hidden from player, but affects dialogue tone)
default aino_approval = 0
default ilmarinen_approval = 0
default lemminkainen_approval = 0

# Story flags
default has_belt = False
default belt_faded = False
default saw_merchant_chest = False

# Functions for game state management

init python:
    def add_item(item_name):
        """Add an item to inventory"""
        global inventory
        if item_name not in inventory:
            inventory.append(item_name)

    def remove_item(item_name):
        """Remove an item from inventory"""
        global inventory
        if item_name in inventory:
            inventory.remove(item_name)

    def add_title(title_name):
        """Add a title to player"""
        global titles
        if title_name not in titles:
            titles.append(title_name)

    def record_decision(decision, outcome):
        """Record a player decision"""
        global decisions
        decisions.append({
            "decision": decision,
            "outcome": outcome
        })

    def get_wisdom_level():
        """Get player's wisdom level based on financial_wisdom score"""
        if financial_wisdom >= 3:
            return "Master of Clear Thinking 🏆"
        elif financial_wisdom >= 2:
            return "Student of Wisdom 📚"
        else:
            return "Seeker of Understanding 🌱"

    def adjust_approval(companion, amount):
        """Adjust companion approval (hidden system)"""
        global aino_approval, ilmarinen_approval, lemminkainen_approval

        if companion == "aino":
            aino_approval += amount
        elif companion == "ilmarinen":
            ilmarinen_approval += amount
        elif companion == "lemminkainen":
            lemminkainen_approval += amount

    def get_companion_tone(companion):
        """Get companion's tone based on approval (not shown to player)"""
        approval = 0
        if companion == "aino":
            approval = aino_approval
        elif companion == "ilmarinen":
            approval = ilmarinen_approval
        elif companion == "lemminkainen":
            approval = lemminkainen_approval

        if approval >= 2:
            return "enthusiastic"
        elif approval >= 0:
            return "neutral"
        elif approval >= -2:
            return "concerned"
        else:
            return "disappointed"
