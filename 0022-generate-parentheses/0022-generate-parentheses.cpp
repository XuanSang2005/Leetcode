class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        generateParentheses(result, "", 0, 0, n);
        return result;
    }

private:
    void generateParentheses(vector<string>& result, string current, int open, int close, int max) {
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }

        if (open < max) {
            generateParentheses(result, current + "(", open + 1, close, max);
        }

        if (close < open) {
            generateParentheses(result, current + ")", open, close + 1, max);
        }
    }
};