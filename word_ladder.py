class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord) 
        word_len = len(beginWord)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(word_len):
            
                pattern = word[:i] + "*" + word[i+1:]
                all_combo_dict[pattern].append(word)

        queue = deque([(beginWord, 1)])  
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()

            for i in range(word_len):

                pattern = current_word[:i] + "*" + current_word[i+1:]

                for neighbor in all_combo_dict[pattern]:
                    if neighbor == endWord:
                        return level + 1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

                
                all_combo_dict[pattern] = []

        return 0
