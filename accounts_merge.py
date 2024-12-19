class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]
        
        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)
            if root1 != root2:
                parent[root2] = root1

        parent = {} 
        email_to_name = {}  
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(first_email, email)
                email_to_name[email] = name
        
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)
        
        merged_accounts = []
        for root, emails in groups.items():
            merged_accounts.append([email_to_name[root]] + sorted(emails))
        
        return merged_accounts
