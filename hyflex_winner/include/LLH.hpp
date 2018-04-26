#ifndef __LLH__HPP__
#define __LLH__HPP__

#include <vector>

template <class Type>
class LLH {
    public:
        std::vector<int> best_found;
        Type total_improvement;
        Type total_worsening;
        std::vector<Type> improvements;
        std::vector<Type> worsenings;
        unsigned time_spent;
        std::vector<unsigned> times;
        
        LLH() {
            total_improvement = (Type)0;
            Type total_worsening = (Type)0;
            unsigned time_spent = 0;
        }
};

#endif 