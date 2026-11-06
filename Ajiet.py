 def browse_items(self):
        if self.current_user is None:
            print("Choose a user first.")
            return

        search = input("Search by item name, or press Enter to see all: ").lower()
        found = False

        for item in self.items:
            if item.is_available() and item.owner != self.current_user:
                if search in item.name.lower():
                    print(
                        item.name,
                        "| Hostel:", item.hostel,
                        "| Owner:", item.owner.name
                    )
                    found = True

        if not found:
            print("No available items found.")

    def request_item(self):
        if self.current_user is None:
            print("Choose a user first.")
            return

        if isinstance(self.current_user, Admin):
            print("Admins cannot borrow items.")
            return

        self.browse_items()
        name = input("Type the item name you want to request: ").lower()

        for item in self.items:
            if item.name.lower() == name and item.is_available():
                if item.owner == self.current_user:
                    print("You cannot request your own item.")
                    return

                request = BorrowRequest(item, self.current_user)
                self.requests.append(request)
                print("Request sent to the owner.")
                return

        print("Available item not found.")

    def review_requests(self):
        if self.current_user is None:
            print("Choose a user first.")
            return

        if isinstance(self.current_user, Admin):
            print("Choose a student to review their requests.")
            return

        found = False

        for request in self.requests:
            if request.item.owner == self.current_user and request.status == "Pending":
                found = True
                print(
                    "\nItem:", request.item.name,
                    "| Requested by:", request.borrower.name
                )

                answer = input("Approve this request? (yes/no): ").lower()

                if answer == "yes":
                    if request.item.borrow():
                        request.status = "Approved"
                        print("Request approved.")
                    else:
                        request.status = "Rejected"
                        print("The item is no longer available.")
                else:
                    request.status = "Rejected"
                    print("Request rejected.")

        if not found:
            print("You have no pending requests.")

    def return_item(self):
        if self.current_user is None:
            print("Choose a user first.")
            return

        for request in self.requests:
            if (request.borrower == self.current_user
                    and request.status == "Approved"):
                print("Item to return:", request.item.name)
                answer = input("Have you returned it? (yes/no): ").lower()

                if answer == "yes":
                    request.item.return_item()
                    request.status = "Returned"
                    print("Return recorded.")
                    return

        print("You have no approved items to return.")
