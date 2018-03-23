// Copyright (c) Steinwurf ApS 2016.
// All Rights Reserved
//
// Distributed under the "BSD License". See the accompanying LICENSE.rst file.

#pragma once

#include <string>
#include <regex>
#include <system_error>

namespace re2
{
class RE2
{
public:
    RE2(const std::string& regex) :
        m_regex(regex)
    { }

    bool ok() const
    {
        return true;
    }

    static bool FullMatch(const std::string& text, const RE2& regex)
    {
        return  std::regex_match(text, regex.m_regex);
    }

    std::string error() const
    {
        return "";
    }
private:
    std::regex m_regex;
};
}